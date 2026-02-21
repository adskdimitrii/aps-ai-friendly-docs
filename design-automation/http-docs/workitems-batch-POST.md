# workitems/batch

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/workitems-batch-POST/

---

# workitems/batch

The new WorkItems are always placed on the queue and later picked up by an engine.

The following limits apply:

Per-engine. These limits are enforced when the engine processes the workitem.

- Processing time (LimitProcessingTime)

- Total size of uncompressed bits for all referenced appbundles (LimitTotalUncompressedAppsSizePerActivity).

Service wide. These limits are enforced during workitem submission.

- Total processing time per month (LimitMonthlyProcessingTimeInHours).

- Maximum number of WorkItems in the request is 100 .

- Activity has to be the same for all WorkItems.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/da/us-east/v3/workitems/batch Authentication Context user context optional Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## Body Structure

id string Id. activityId * string Reference to the Activity that this WorkItem will invoke.  Examples: MyPlot+Prod (an Activity created by the caller) or Autodesk.PlotToPdf (an Activity created by someone else and shared with this caller). arguments object Arguments of the WorkItem. Named parameters of an Activity have corresponding named arguments of a WorkItem. * any of Type: dictionary<string, * > StringArgument object Simple string argument. This class represents string argument both in the workitem and job. value string XrefTreeArgument object Represents an HTTP request argument in the workitem (see also BoundXrefTreeArgument).
Note that when specifying the Activity with the parameter onDemand=âtrueâ this XrefTreeArgument will be ignored. optional boolean Argument optionality. Failure to download optional input arguments is OK.
Failure to find or upload optional output arguments is OK. Defaults to false. localName string Provides default name of the file or folder on the processing server for this argument. The âlocal nameâ of an argument is determined by the following algorithm: Use XrefTreeArgumentBase.LocalName if non-empty, otherwise next step. Use Autodesk.Das.Shared.Models.Parameter.LocalName if non-empty, otherwise next step Fail if Autodesk.Das.Shared.Models.Request.Url is a data url , otherwise next step. Use the Content-Disposition header provided by Autodesk.Das.Shared.Models.Request.Url if the argument is an input (verb=get) and header is present, otherwise next step. Use the last segment Autodesk.Das.Shared.Models.Request.Url if the argument is an input (verb=get) and last segment of Autodesk.Das.Shared.Models.Request.Url is a filename (i.e. contains valid filename characters only and has an extension), otherwise next step. Use a unique generated name. pathInZip string Denotes the âmain fileâ in a zip. This attribute together with the Autodesk.Das.Shared.Models.Parameter.Zip attribute determine how zip files are handled.
The following table describes the behavior: # Activity Workitem Arg direction Comments 1 zip==true pathInZip!=null input Zip is uncompressed to the folder specified in localname . Any path reference to this argument will expand to full path of pathInZip . 2 zip==false pathInZip!=null input Zip is uncompressed to the folder specified in localname . Any path reference to this argument will expand to full path of pathInZip . 3 zip==true pathInZip==null input If zip is provided then it is uncompressed to the folder specified in localname . Any path reference to this argument will expand to full path of localName . 4 zip==false pathInZip==null input If zip is provided then it is left compressed. Any variable referencing this argument will expand to full path of localName . 5 zip==true pathInZip!=null output Workitem will be rejected. 6 zip==false pathInZip!=null output Workitem will be rejected. 7 zip==true pathInZip==null output Output(s) at localName will be zipped if localName is a folder. 8 zip==false pathInZip==null output Output at localName will not be zipped. references array: XrefTreeArgument requestContent string Define request content. For example, to receive data, POST/PUT requires request body
which can be passed by ârequestContentâ. url * string Url. headers object Headers. * string Type: dictionary<string, * > verb enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: get , head , put , post , patch , read multiparts object Provide multipart post method to upload the results and multiparts can be empty if there is no âparameterâ to provide. It supports Box , Google Drive and Amazon Simple Storage Service (S3) services. Examples of using argument âmultipartsâ: Box: âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ} Google Drive: âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}} Amazon Simple Storage Service (S3): âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ} * object Type: dictionary<string, * > signatures object Signatures for various WorkItem attributes. activityId string Digital signature of the ActivityId. The client must supply this when using a 3-legged oauth token for submitting a WorkItem. baseUrls array: object Digitally signed base urls that are allowed in the WorkItem. The client may supply these when using a 3-legged oauth token for submitting a WorkItem. url * string The Url value. signature * string The signature calculated for Url. limitProcessingTimeSec int Max duration of processing in seconds per workitem (includes download and upload time).

Failure to download optional input arguments is OK.
Failure to find or upload optional output arguments is OK.

Defaults to false.

- Use XrefTreeArgumentBase.LocalName if non-empty, otherwise next step.

- Use Autodesk.Das.Shared.Models.Parameter.LocalName if non-empty, otherwise next step

- Fail if Autodesk.Das.Shared.Models.Request.Url is a data url , otherwise next step.

- Use the Content-Disposition header provided by Autodesk.Das.Shared.Models.Request.Url if the argument is an input (verb=get) and header is present, otherwise next step.

- Use the last segment Autodesk.Das.Shared.Models.Request.Url if the argument is an input (verb=get) and last segment of Autodesk.Das.Shared.Models.Request.Url is a filename (i.e. contains valid filename characters only and has an extension), otherwise next step.

- Use a unique generated name.

# Activity Workitem Arg direction Comments 1 zip==true pathInZip!=null input Zip is uncompressed to the folder specified in localname . Any path reference to this argument will expand to full path of pathInZip . 2 zip==false pathInZip!=null input Zip is uncompressed to the folder specified in localname . Any path reference to this argument will expand to full path of pathInZip . 3 zip==true pathInZip==null input If zip is provided then it is uncompressed to the folder specified in localname . Any path reference to this argument will expand to full path of localName . 4 zip==false pathInZip==null input If zip is provided then it is left compressed. Any variable referencing this argument will expand to full path of localName . 5 zip==true pathInZip!=null output Workitem will be rejected. 6 zip==false pathInZip!=null output Workitem will be rejected. 7 zip==true pathInZip==null output Output(s) at localName will be zipped if localName is a folder. 8 zip==false pathInZip==null output Output at localName will not be zipped.

#

Activity

Workitem

Arg direction

Comments

For example, to receive data, POST/PUT requires request body
which can be passed by ârequestContentâ.

It supports Box , Google Drive and Amazon Simple Storage Service (S3) services.

Examples of using argument âmultipartsâ:

Box:

âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ}

Google Drive:

âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}}

Amazon Simple Storage Service (S3):

âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ}

### Response

## HTTP Status Code Summary

200 OK Successfully create a batch of new WorkItems. 400 Bad Request The request is invalid. 403 Forbidden The user is not authorized to create the WorkItem. 413 Payload is too large.

### Response

## Body Structure (200)

status enum:string Status value of a WorkItem.
Possible values: pending , inprogress , cancelled , failedLimitProcessingTime , failedDownload , failedInstructions , failedUpload , failedUploadOptional , success progress string The current status of the workitem. reportUrl string The detailed report about the workitem, report url is valid for 24 hours from first receiving it. stats object Basic statistics about workitem processing. timeQueued datetime: ISO 8601 The time in UTC when the workitem was queued. timeDownloadStarted datetime: ISO 8601 The time in UTC when the system started processing the workitem by transferring input data to the processing node. timeInstructionsStarted datetime: ISO 8601 The time in UTC when the system finished downloading input and started processing instructions from the Activity associated with this workitem. timeInstructionsEnded datetime: ISO 8601 The time in UTC when the system finished executing instructions and started uploading outputs. timeUploadEnded datetime: ISO 8601 The time in UTC when the system finished uploading outputs. timeFinished datetime: ISO 8601 The time in UTC when the system finished the workitem and reported the status. bytesDownloaded int The file size of bytes the job downloads for input. bytesUploaded int The file size of bytes the job uploads for output. id string A GUID used to identify the WorkItem submitted successfully.

## Example

Successfully create a batch of new WorkItems.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/workitems/batch' \ - X 'POST' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ - H 'Content-Type: application/json' \ - d '[ { "activityId": "owner.ChangeParams+prod", "arguments": { "InventorDoc": { "url": "https://s3-us-east-1.amazonaws.com/inventorio-prod/documentation/APIBasics/Box.ipt" }, "InventorParams": { "url": "data:application/json,{ \" height \" : \" 16 in \" , \" width \" : \" 10 in \" }" }, "OutputIpt": { "url": "https://developer.api.autodesk.com/oss/v2/signedresources/2922c578-da22-4a35-a943-6cfeb4484009?region=US", "headers": { "Authorization": "", "Content-type": "application/octet-stream" }, "verb": "put" }, "OutputBmp": { "url": "https://developer.api.autodesk.com/oss/v2/signedresources/a4717873-88db-49c1-9f41-98705a199622?region=US", "headers": { "Authorization": "", "Content-type": "application/octet-stream" }, "verb": "put" } } } ]'
```

### Response

```
[ { "status" : "pending" , "stats" : { "timeQueued" : "2022-01-01T00:00:00Z" }, "id" : "wi1234" } ]
```
