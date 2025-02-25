use std::fs;
use std::error::Error;
use regex::Regex;


pub fn part1(input: &str) -> u32 {
    // create a function to scan string, look fro only mul(\d[1-3],\d[1-3]) I guess, then
    // multiply and add those all up?
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    let mut result = 0;
    for (_, [num1, num2]) in re.captures_iter(input).map(|cg| cg.extract()) {
        let m = num1.parse::<u32>().unwrap() * num2.parse::<u32>().unwrap();
        result += m;
    }
    result

}


pub fn part2(input: &str) -> u32 {
    1
}

pub fn load_input(path: &str) -> Result<String, Box<dyn Error>> {
    let message: String = fs::read_to_string(path)?;
    Ok(message)
}
