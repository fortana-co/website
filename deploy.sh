./build.sh

bucketname='fortana-web'

aws s3 cp --recursive public s3://${bucketname} --acl public-read

aws cloudfront create-invalidation --distribution-id E3PEBWAFIZMLTL --paths '/*'
