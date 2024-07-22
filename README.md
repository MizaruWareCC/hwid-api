WARING<br />
This is being used to fight people using https debuggers to create dynamic, hwid-depended response.<br />
If you will use this, please change this method, because people knowing about this repository can use this method for auto-response.<br />
<br />
API docs:<br />
root/cheker: GET<br />
-Query<br />
 -hwid=str // HWID or any other data<br />
-Responses<br />
 -400, Invalid Body // HWID isn't provided, or its type isn't str<br />
 -404, Not Found // HWID isnt found, or it's outdated<br />
 -200, returns hash generated on HWID base // Success<br />
<br />
root/create_hwid: POST<br />
-Json<br />
{<br />
	"secure": "str",<br />
	"untill": "timestamp",<br />
	"hwid": "str"<br />
}<br />
-Responses<br />
 -400, Invalid Body // Json isn't a dict (eg. list), timestamp isnt valid<br />
 -403, Forbidden // Secure isn't correct<br />
 -204, No Response, // Success<br />
<br />
