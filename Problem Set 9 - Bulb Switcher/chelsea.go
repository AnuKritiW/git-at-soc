func bulbSwitch(n int) int {
    // Find how many factors does i have
    // If odd number of factors, blub is on ==> only if i is a square!
    // If even number of factors, bulb is off
    // So we just need to find how many squares are there
    
    lit := 0
    for i := 1; i <= n; i++ {
        if i * i <= n {
            lit++
        } else {
            break
        }
    }
    return lit
}