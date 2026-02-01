// Find the bugs and fix them!

const name = "Alice";
const her location = "the Queen's Garden";
const size = Small;
const minutesInWonderland = "60";

console.log(name + "is currently in" + her location + "and is" + size);
console.log("She has been in Wonderland for" + minutesInWonderland + "minutes.");

console.log("");

location = "the White Rabbit's House";
size = "Large";
minutesInWonderland = minutesInWonderland + "60";

console.log(name + "moved to" + her location + " and is now" + size);
console.log("She has been in Wonderland for" + minutesInWonderland + "minutes.");

// Expected output when fixed:

// Alice is currently in the Queen's Garden and is Small
// She has been in Wonderland for 60 minutes.
//
// Alice moved to the White Rabbit's House and is now Large
// She has been in Wonderland for 120 minutes.