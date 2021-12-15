FROM elasticsearch:5.5.2

#add country index to container
ADD geonames_index.tar.gz /usr/share/elasticsearch/

#configure elasticsearch
ADD elasticsearch.yml /usr/share/elasticsearch/config