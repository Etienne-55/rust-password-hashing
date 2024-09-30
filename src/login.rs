use std::io;
use sha2::{Sha256, Digest};

pub fn add_user() -> (String, String) {

    let _email = String::new();
    let _password = String::new();


    println!("Enter your email: ");
    let mut email = String::new();
    io::stdin().read_line(&mut email).expect("Failed to read line.");

    println!("Enter your password: ");
    let mut password = String::new();
    io::stdin().read_line(&mut password).expect("Failed to read line.");

    (email.trim().to_string(), password.trim().to_string())

}

pub fn hash_credentials(email: &str, password: &str) {

    let mut email_hasher = Sha256::new();
    email_hasher.update(email);
    let email_hash = email_hasher.finalize();

    let mut password_hasher = Sha256::new();
    password_hasher.update(password);
    let password_hash = password_hasher.finalize();

    println!("hashed email: {:x}", email_hash);
    println!("hashed pasword: {:x}", password_hash);
}