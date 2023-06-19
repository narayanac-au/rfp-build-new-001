// process.argv.forEach(function (val, index, array) {
//     console.log(index + ': ' + val);
//     console.log("Current directory:", process.cwd());
//     console.log('-----------')
// });

function merge_documents(){
    var DocxMerger = require('docx-merger');
    
    var fs = require('fs');
    var path = require('path');

    var files_arr = []
    process.argv.forEach(function (val, index, array) {
        console.log(index + ': ' + val);
        console.log("Current directory:", process.cwd());
        console.log('-----------')
        if (index == 0 | index == 1) {
            console.log('skip 0 and 1')
        } else {
            let var_string = 'file' + index.toString()
            let file_path = process.cwd() + val
            var_string = fs
                .readFileSync(path.resolve(__dirname, file_path), 'binary');
            files_arr.push(var_string)
        }
    });
    
    // var file1 = fs
    //     .readFileSync(path.resolve(__dirname, 'C:/Users/narayanac/Documents/rfp-backup/current-rfp/RFP/test_image_file_PuATo0v.docx'), 'binary');
    
    // var file2 = fs
    //     .readFileSync(path.resolve(__dirname, 'C:/Users/narayanac/Documents/rfp-backup/current-rfp/RFP/TEST-MAY-04-2023-001_Healthcare_AU_Implementation Approach.docx'), 'binary');
    
    // var docx = new DocxMerger({},[file1,file2]);
    console.log(files_arr, 'files array')
    var docx = new DocxMerger({},files_arr);
    
    
    //SAVING THE DOCX FILE
    
    docx.save('nodebuffer',function (data) {
        // fs.writeFile("output.zip", data, function(err){/*...*/});
        fs.writeFile("output-node-merger-v4.docx", data, function(err){/*...*/});
    });
    return 'output-node-merger.docx'
}

run = merge_documents()

// return 'output-node-merger.docx'