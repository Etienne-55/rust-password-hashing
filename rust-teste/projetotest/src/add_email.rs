use sha2::{Sha256, Digest};

fn main() {
    let email = "example@example.com";
    let password = "supersecretpassword";

    let mut hasher = Sha256::new();

    hasher.update(email);
    let email_hash = hasher.finalize_reset();

    hasher.update(password);
    let password_hash = hasher.finalize();

    println!("Email hash: {:x}", email_hash);
    println!("Password hash: {:x}", password_hash);
}