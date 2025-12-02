use std::fs;

pub fn get_data(filepath: &str) -> Vec<String> {
    match fs::read_to_string(filepath) {
        Ok(content) => content.lines().map(|line| line.to_string()).collect(),
        Err(e) => panic!("Errore {}, con lettura di {}", e, filepath),
    }
}
