'use strict';

const fs = require('fs');

//store entire study mapped json in new var
let originalMapping = {
"mapping": [
   { "attribute": "time",
      "code": 25220,
      "codeSystem": "LOINC",
      "item": "type",
      "question": "lab collect time"

   },
   {  "attribute": "time",
      "code": 25740,

      "codeSystem": "LOINC",
      "item": "type",
      "question": "lab collect time"
      
   },
   {  "attribute": "time",
      "code": 22740,

      "codeSystem": "LOINC",
      "item": "type",
      "question": "lab collect time"
   },
   {  "attribute": "date",
      "code": 15740,

      "codeSystem": "LOINC",
      "item": "type",
      "question": "lab collect time"
   },
   {  "attribute": "time",
      "code": 25740,

      "codeSystem": "LOINC",
      "item": "type",
      "question": "lab collect time"
      }

   ]
};
// iterate through json objects to filter and remove items that contain key, value attribute: "DATE" and key = code 
 originalMapping.mapping.forEach(item => {
     if (item.attribute === "DATE" && item.hasOwnProperty('code')){
         delete item.attribute;
         delete item.code;
        }
    });

//write to newMap file. copy and paste to body of Postman PUT, then run study mapping GET to confirm undesired items are no longer mapped.
 let data = JSON.stringify(originalMapping, null, 4);
 fs.writeFileSync('newMap.json', data);
