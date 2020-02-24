## Quick Start

Docker build
Docker run

## Test

cd test
docker push iconnor/removetag:sampletag
curl -X POST -H "Content-Type: application/json" -d @sample_merge.json 'http://localhost:5000/tags?username=iconnor&password=$PASSWORD&organization=iconnor&image=removetag'
