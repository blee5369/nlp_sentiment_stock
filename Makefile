.PHONY: default 
default: image 

.PHONY: image
image: 
	docker build -t mordecai .

.PHONY: develop
develop: image 
	docker run -d -p 127.0.0.1:9200:9200 -v $(pwd)/geonames_index/:/usr/share/elasticsearch/data elasticsearch:5.5.2
