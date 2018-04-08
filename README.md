# RMon - a redis server monitor



|名称	           |URL	              |HTTP 方法	|成功状态码|	失败状态码|  
|:----------------|-------------------|:-----------:|---------|:-----------:|
|获取服务器列表	   |/servers/	          |GET	    |   200	   |          500|  
|创建服务器	       |/servers/	          |POST	     |  201	  |          400|  
|获取服务器	       |/servers/server_id	  |GET	    |   200	  |          404|  
|更新服务器	       |/servers/server_id	  |PUT	    |   200    |     404/400|  
|删除服务器	       |/servers/server_id 	  |DELETE	|   204	  |           404|  
|获取服务器监控数据 |/servers/server_id/metrics	|GET  |   200	|      404/500|  
