use std::io;
use sha2::{Sha256, Digest};


struct User {
    email: String,
    password: String,
}



pub fn add_user(email, password) {

    println!("Enter your email: ");
    let mut email = String::new();
    io::stdin()
        .read_line(&mut email)
        .expect("Failed to read line.");
    let email = email.trim();

    println!("Enter your password: ");
    let mut password = String::new();
    io::stdin()
        .read_line(&mut password);
        .expect("Failed to read line.")    
    let password = password.trim();   
}


pub fn hash_credentials(add_user) {
    let mut = email 
    let mut = password

    let mut hasher = Sha256::new();

    hasher.update(email);
    let email_hash = hasher.finalize_reset();

    hasher.update(password);
    let password_hash = hasher.finalize_reset();

    println!("hashed pasword{}", password_hash);
}