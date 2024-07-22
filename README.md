WARING
This is being used to fight people using https debuggers to create dynamic, hwid-depended response.
If you will use this, please change this method, because people knowing about this repository can use this method for auto-response.

API docs:
root/cheker: GET
-Query
 -hwid=str // HWID or any other data
-Responses
 -400, Invalid Body // HWID isn't provided, or its type isn't str
 -404, Not Found // HWID isnt found, or it's outdated
 -200, returns hash generated on HWID base // Success

root/create_hwid: POST
-Json
{
	"secure": "str",
	"untill": "timestamp",
	"hwid": "str"
}
-Responses
 -400, Invalid Body // Json isn't a dict (eg. list), timestamp isnt valid
 -403, Forbidden // Secure isn't correct
 -204, No Response, // Success
