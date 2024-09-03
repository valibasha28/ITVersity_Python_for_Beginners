def log(message, level='INFO'):
    print(f"[{level}] {message}")

log("User logged in..!")
log("Server started", "DEBUG")