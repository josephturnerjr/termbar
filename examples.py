from termbar import TermBar

if __name__ == "__main__":
    vals = [
            ("January", 10),
            ("February", 20),
            ("March", 30),
            ("April", 0),
            ("May", 30),
            ("June", 30),
            ("July", 50),
            ("August", 60),
            ("September", -10),
            ("October", -20),
            ("November",55),
            ("December", 23),
           ]
    # Full-on!
    a = TermBar(vals, write_axis_labels=True, write_values=True, title="Monthly Chart")
    a.draw()
