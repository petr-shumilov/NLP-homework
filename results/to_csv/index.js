const jsonFile 			= require('../result.json');
const createCsvWriter 	= require('csv-writer').createObjectCsvWriter;

const csvWriter = createCsvWriter({
    path: '../result.csv',
    fieldDelimiter: ';',
    header: [
        {id: 'lemma', title: 'LEMMA'},
        {id: 'words', title: 'WORDS'},
     	{id: 'frequency', title: 'FREQUENCY'} 
    ]
});
 
let lemmarFreq = []
for (let lemma in jsonFile) {
	lemmarFreq.push([jsonFile[lemma].length, lemma]);
}

console.log('Sorting...'); 
lemmarFreq.sort((a, b) => b[0] - a[0]);

console.log('Formatting for writing to csv');

let records = [];
for (let i in lemmarFreq) {
	records.push({
		lemma: lemmarFreq[i][1],	
		words: jsonFile[lemmarFreq[i][1]].join(','),
		frequency: lemmarFreq[i][0]	
	})
}

console.log('Writing...');
csvWriter.writeRecords(records).then(() => {
	console.log('...Done');
});
 
