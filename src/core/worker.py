"""
Multi-threaded Worker for Scraping Tasks
Handles asynchronous scraping operations with thread safety
"""
import threading
import queue
import asyncio
from typing import Callable, Any, Optional
from src.utils.logger import Logger


class ScraperWorker(threading.Thread):
    """Thread worker for executing scraping tasks"""
    
    def __init__(
        self,
        worker_id: int,
        task_queue: queue.Queue,
        result_queue: queue.Queue,
        scraper_func: Callable,
        **kwargs
    ):
        """
        Initialize worker thread
        
        Args:
            worker_id: Unique identifier for this worker
            task_queue: Queue containing tasks to process
            result_queue: Queue to put results in
            scraper_func: Async function to execute for each task
            **kwargs: Additional arguments to pass to scraper_func
        """
        super().__init__(daemon=True)
        self.worker_id = worker_id
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.scraper_func = scraper_func
        self.kwargs = kwargs
        self._stop_event = threading.Event()
        self.logger = Logger.get_logger(f"Worker-{worker_id}")
    
    def run(self):
        """Main worker loop - runs in separate thread"""
        self.logger.info(f"Worker {self.worker_id} started")
        
        # Create new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            loop.run_until_complete(self._async_run())
        except Exception as e:
            self.logger.error(f"Worker {self.worker_id} error: {e}")
        finally:
            loop.close()
            self.logger.info(f"Worker {self.worker_id} stopped")
    
    async def _async_run(self):
        """Asynchronous worker loop"""
        while not self._stop_event.is_set():
            try:
                # Get task with timeout
                task = self.task_queue.get(timeout=1)
                
                # Check for poison pill (None = stop signal)
                if task is None:
                    self.logger.info(f"Worker {self.worker_id} received stop signal")
                    break
                
                self.logger.info(f"Worker {self.worker_id} processing: {task}")
                
                # Execute the scraping function
                result = await self.scraper_func(task, **self.kwargs)
                
                # Put result in result queue
                self.result_queue.put({
                    'status': 'success',
                    'task': task,
                    'result': result,
                    'worker_id': self.worker_id
                })
                
                self.logger.info(f"Worker {self.worker_id} completed: {task}")
                
            except queue.Empty:
                # No tasks available, continue waiting
                continue
                
            except Exception as e:
                # Error processing task
                self.logger.error(f"Worker {self.worker_id} error processing task: {e}")
                self.result_queue.put({
                    'status': 'error',
                    'task': task if 'task' in locals() else None,
                    'error': str(e),
                    'worker_id': self.worker_id
                })
                
            finally:
                # Mark task as done
                try:
                    self.task_queue.task_done()
                except:
                    pass
    
    def stop(self):
        """Signal the worker to stop"""
        self._stop_event.set()


class WorkerPool:
    """Manages a pool of worker threads"""
    
    def __init__(self, num_workers: int, scraper_func: Callable, **kwargs):
        """
        Initialize worker pool
        
        Args:
            num_workers: Number of worker threads to create
            scraper_func: Async function to execute for each task
            **kwargs: Additional arguments to pass to scraper_func
        """
        self.num_workers = num_workers
        self.scraper_func = scraper_func
        self.kwargs = kwargs
        
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.workers = []
        self.logger = Logger.get_logger("WorkerPool")
    
    def start(self):
        """Start all worker threads"""
        self.logger.info(f"Starting {self.num_workers} workers")
        
        for i in range(self.num_workers):
            worker = ScraperWorker(
                worker_id=i,
                task_queue=self.task_queue,
                result_queue=self.result_queue,
                scraper_func=self.scraper_func,
                **self.kwargs
            )
            worker.start()
            self.workers.append(worker)
    
    def add_task(self, task: Any):
        """Add a task to the queue"""
        self.task_queue.put(task)
    
    def add_tasks(self, tasks: list):
        """Add multiple tasks to the queue"""
        for task in tasks:
            self.add_task(task)
    
    def get_result(self, timeout: Optional[float] = None) -> Optional[dict]:
        """Get a result from the result queue"""
        try:
            return self.result_queue.get(timeout=timeout)
        except queue.Empty:
            return None
    
    def stop(self, wait: bool = True, force: bool = False):
        """
        Stop all workers
        
        Args:
            wait: If True, wait for workers to finish current tasks
            force: If True, forcefully stop workers immediately (daemon threads will die with main thread)
        """
        self.logger.info("Stopping all workers" + (" (forced)" if force else ""))
        
        if force:
            # Force stop: signal all workers to stop immediately
            for worker in self.workers:
                worker.stop()
            
            # Clear task queue to prevent workers from picking up new tasks
            while not self.task_queue.empty():
                try:
                    self.task_queue.get_nowait()
                    self.task_queue.task_done()
                except queue.Empty:
                    break
            
            # Don't wait - let daemon threads die naturally
            # (they will be killed when main thread exits)
            self.workers.clear()
            self.logger.info("All workers force-stopped (daemon threads)")
        else:
            # Graceful stop: send poison pills
            for _ in range(self.num_workers):
                self.task_queue.put(None)
            
            # Stop all workers
            for worker in self.workers:
                worker.stop()
            
            # Wait for workers to finish if requested
            if wait:
                for worker in self.workers:
                    worker.join(timeout=5)
            
            self.workers.clear()
            self.logger.info("All workers stopped" + (" gracefully" if wait else ""))
    
    def is_active(self) -> bool:
        """Check if any workers are still active"""
        return any(worker.is_alive() for worker in self.workers)
    
    def tasks_pending(self) -> int:
        """Get number of pending tasks"""
        return self.task_queue.qsize()
    
    def results_available(self) -> int:
        """Get number of available results"""
        return self.result_queue.qsize()
