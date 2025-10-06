call_count = 0
def track_calls():
    global call_count
    call_count += 1
    print(f"Function called {call_count} times.")
track_calls()
track_calls()
track_calls()
track_calls()
track_calls()