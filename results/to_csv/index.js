const lemmantizedFile 	= require('../result.json');
const frequencyFile 	= require('../frequency.json');
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
 
let lemmaFreq = []
for (let lemma in frequencyFile) {
	lemmaFreq.push([frequencyFile[lemma], lemma]);
}

console.log('Sorting...'); 
lemmaFreq.sort((a, b) => b[0] - a[0]);

console.log('Formatting for writing to csv');

let records = [];
let count = 0;
for (let i in lemmaFreq) {
	try {
		let lemma = lemmaFreq[i][1];
		records.push({
			lemma,	
			words: lemmantizedFile[lemma].join(','),
			frequency: lemmaFreq[i][0]	
		})
	}
	catch (e) {
		continue;
	}
}

console.log('Writing...');
csvWriter.writeRecords(records).then(() => {
	console.log('...Done');
});
 
