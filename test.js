var bayes = require('bayes')

var classifier = bayes()

const csv = require('csv-parser');
const fs = require('fs');

fs.createReadStream('data/trojmiasto.csv')
  .pipe(csv())
  .on('data', (row) => {
    //console.log(row['Title'], row["Category"]);
    classifier.learn(row['Title'], row["Category"])
    //console.log(classifier.categorize('Donald tusk to kurwa'))
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
    console.log(classifier.categorize('Miękka i wilgotna skóra, a w żołądku ostatni, niestrawiony posiłek. Niezwykła mumia po 2000 lat'))
  });


  var stdin = process.openStdin();

  stdin.addListener("data", function(d) {
      // note:  d is an object, and when converted to a string it will
      // end with a linefeed.  so we (rather crudely) account for that
      // with toString() and then trim()
      console.log(classifier.categorize(d.toString()))
    });

// now ask it to categorize a document it has never seen before

//console.log(classifier.categorize('awesome, cool, amazing!! Yay.'))
// => 'positive'

// serialize the classifier's state as a JSON string.
//var stateJson = classifier.toJson()

// load the classifier back from its JSON representation.
//var revivedClassifier = bayes.fromJson(stateJson)
