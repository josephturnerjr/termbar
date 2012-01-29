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
    print "TermBar draws bar charts in ascii in the terminal. Like this:"
    # Full-on!
    a = TermBar(vals, write_labels=True, write_axis_labels=True, write_values=True, title="Monthly Chart")
    a.draw()
    print "You can go minimal..."
    a = TermBar(vals)
    a.draw()
    print "...add a title..."
    a = TermBar(vals, title="This is the title")
    a.draw()
    print "...add series labels..."
    a = TermBar(vals, write_labels=True, title="This is the title")
    a.draw()
    print "...add data labels..."
    a = TermBar(vals, write_labels=True, write_values=True, title="This is the title")
    a.draw()
    print "...and add axis labels."
    a = TermBar(vals, write_labels=True, write_axis_labels=True, write_values=True, title="This is the title")
    a.draw()
    print "...and make it look objectively awful."
    a = TermBar(vals, write_labels=True, write_axis_labels=True, write_values=True, title="This is the title", fill_char="]", delim="^", y_axis_mark=">")
    a.draw()
