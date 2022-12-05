use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


pub fn part1(input: io::Result<io::Lines<io::BufReader<File>>>) -> i32 {
    let mut elves = Vec::new();
    let mut s = 0;
    let mut max = 0; 
    // This is unwrapping to a io::Lines, which yields instances of io::Result<String>
    for line in input.unwrap() {
        if line.as_ref().unwrap().as_str().is_empty() {
            // check s > max
            if s > max {
                max = s;
            }
            elves.push(s);
            s = 0;
            continue
        }
        else {
            let num = line.unwrap();
            s += num.parse::<i32>().unwrap();
        }
    }
    max 
}



// load to bufreader result
pub fn load_input<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}