from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#API key info


wait_time = 1

#save
animalName     = sys.argv[1]
pprint(animalName)
savedir  = "./" + animalName
flickr = FlickrAPI(key, secret, format='parsed-json')
result   = flickr.photos.search(
  text        = animalName,
  per_page    = 400,
  media       = 'photos',
  sort        = 'relevance',
  safe_search = 1,
  extras      = 'url_q, licence'
)

photos = result['photos']
pprint(photos)
