##Thread

###前言
摘抄记录，必备不时之需

###map

map 函数一手包办了序列操作、参数传递和结果保存等一系列的操作，可以轻松实现并行化操作。
io密集型适用多进程，cpu密集型适合多线程，map是多线程。线程设置经验值2n-1，其中n为核数。

	import urllib2 
	from multiprocessing.dummy import Pool as ThreadPool 
	 
	urls = [
	    'http://www.python.org', 
	    'http://www.python.org/about/',
	    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
	    'http://www.python.org/doc/',
	    'http://www.python.org/download/',
	    # etc.. 
	    ]
	 
	# Make the Pool of workers
	pool = ThreadPool(4) 
	# Open the urls in their own threads
	# and return the results
	results = pool.map(urllib2.urlopen, urls)
	#close the pool and wait for the work to finish 
	pool.close() 
	pool.join() 