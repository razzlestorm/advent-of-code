use std::fs;
use std::error::Error;


pub fn part1(input: &str) -> u32 {
    1
}


pub fn part2(input: &str) -> u32 {
    1
}

pub fn load_input(path: &str) -> Result<String, Box<dyn Error>> {
    let message: String = fs::read_to_string(path)?;
    Ok(message)
}
