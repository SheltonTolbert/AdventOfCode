const fs = require("fs");

function isUppercase(char) {
  return char.toUpperCase() === char;
}

function solve(data) {
  let result = 0;
  const set1 = new Set();
  const set2 = new Set();

  data.split("\n").forEach((rucksack, index) => {
    rucksack.split("").forEach((char) => {
      if (index % 3 == 2 && set2.has(char) && set1.has(char)) {
        result += char.toLowerCase().charCodeAt(0) - 96 + (isUppercase(char) ? 26 : 0);
        set1.clear();
        set2.clear();
      } else if (index  % 3 == 1){
        set2.add(char)
      } else if (index % 3 == 0){
        set1.add(char)
      }
    });
  });
  return result;
}

const filename = process.argv[2];
fs.readFile(filename, "utf8", function (err, data) {
  if (err) throw err;
  console.log(solve(data));
});
