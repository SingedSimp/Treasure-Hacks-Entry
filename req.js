// I was gonna have this run on sashido backend, but I had too many issues with the parse backend, so it's running locally
var fs = require('fs')
let url = fs.readFileSync('./url.txt', 'utf8')
console.log(url)
let out;
const TeachableMachine = require("@sashido/teachablemachine-node");
const model = new TeachableMachine({
    modelUrl: "https://teachablemachine.withgoogle.com/models/78mt_CuhY/"
});

model.classify({
    imageUrl: url,
  }).then((predictions) => {
    console.log("Predictions:", predictions);
    console.log(predictions[0])
    out = JSON.stringify(predictions);
    fs.writeFileSync('./output.txt', out);
  }).catch((e) => {
    console.log("ERROR", e);
  });