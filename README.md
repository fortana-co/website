# Fortana's website

## Development
`npm install`, then `npm run dev`. Then open `index.html` in your browser.

## Lead form
Handled by [this Lambda function](https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/functions/handleLead), which is invoked by [API Gateway](https://us-west-2.console.aws.amazon.com/apigateway/home?region=us-west-2#/apis/kf8f3w2kg1/resources/tujpyj4p4k).

## Deployment
<https://fortana.co> is served by an S3 bucket behind Amazon CloudFront. Just run `npm run deploy`.
