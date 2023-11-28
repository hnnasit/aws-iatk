import { PhysicalIdFromStackParams, Request, Response, RequestMetadata } from "./iatk";
const { execSync } = require('child_process');

let params: PhysicalIdFromStackParams = {
  logicalResourceId:"StockCheckerFunction",
  stackName:"sam-remote-invok-sfn",
  region:"us-east-1",
  profile:""
};

console.log("Hello IATK in typescript");
console.log(params);

let metadata: RequestMetadata = {
  client:"python",
  version:"0.1.0",
  caller:"get_physical_id",
  clientVersion:"18.15.0"
}

let request: Request = {
  jsonrpc:"2.0",
  id:"12",
  method:"get_physical_id",
  params:params,
  metadata:metadata
};

let request_bytes = Request.toBinary(request);
try {
  const result = execSync('/Users/hnnasit/workspace/aws-iatk/python-client/src/iatk_service/iatk', { input: request_bytes});
  let response = Response.fromBinary(result)
  console.log(response);
  
  } catch (error) {
      console.error("errorrrr");
      
  }