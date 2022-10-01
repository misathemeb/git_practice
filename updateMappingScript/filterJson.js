'use strict';

const fs = require('fs');

//store entire study mapped json in new var
let originalMapping = {
    "mapping": [
        {  "attribute": "time",
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
// map through json objects to filter out items that will continue to be mapped. 
const newJson = originalMapping.mapping.filter( item => {
       return !(item.attribute == "time" && item.code)
});

//write to newMap file. copy and paste to body of Postman PUT, then run study mapping GET to confirm undesired items are no longer mapped.
let data = JSON.stringify(newJson, null, 4);
fs.writeFileSync('newMap.json', data);

console.log(newJson)

