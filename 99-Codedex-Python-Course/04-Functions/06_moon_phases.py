"""

Instructions

Why are there so many Moon emojis? Each one represents a different Moon phase, the shape of the Moon's sunlit portion as viewed from the Earth.

Write a moon_phase() function that takes in a phase parameter of the Moon phase name given below and returns the correct Moon emoji for it:

    New Moon → 🌑
    Waxing Crescent → 🌒
    First Quarter → 🌓
    Waxing Gibbous → 🌔
    Full Moon → 🌕
    Waning Gibbous → 🌖
    Last Quarter → 🌗
    Waning Crescent → 🌘

Else an invalid phase name is passed to moon_phase(), return 'Invalid moon phase'.

Call the moon_phase() to test it out:

"""


moon_phases_dict = {
    "New Moon" : "🌑",
    "Waxing Crescent" : "🌒",
    "First Quarter" : "🌓",
    "Waxing Gibbous" : "🌔",
    "Full Moon" : "🌕",
    "Waning Gibbous" : "🌖",
    "Last Quarter" : "🌗",
    "Waning Crescent" : "🌘"
}

def moon_phase(phase):
    return moon_phases_dict.get(phase , "Invalid moon phase")

answer = moon_phase('Last Quarter')
print(answer)

# Output: 🌑



