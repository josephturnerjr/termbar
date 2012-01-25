def draw_graph(series, width=40, title="", write_axis_labels=False, 
               write_values=False, fill_char="#", delimiter="|"):
    """
    Draws a left-right bar graph in the terminal
    series should be a list of tuples:
        (label, value)
    """
    max_label_len = max([len(s[0]) for s in series])
    max_value = max([s[1] for s in series])
    min_value = min([s[1] for s in series])
    if min_value > 0:
        min_value = 0
    val_range = max_value - min_value
    print
    if title:
        print "%s%s%s" % (" " * (max_label_len + 2), 
                          " " * ((width - len(title))/2), 
                          title)
    zero = int(width * (float(0 - min_value) / val_range))
    print "%s%s+%s" % (" " * (max_label_len + 2), "_" * zero, "_" * (width - zero))
    for label, value in series:
        lpad = max_label_len - len(label)
        if write_values:
            rlabel = " %s" % (value,)
        else:
            rlabel = ""
        fill_len = int(width * (float(value - min_value) / val_range))
        to_print = "%s%s %s%s%s%s%s" % (" " * lpad, label, delimiter, 
                                        fill_char * fill_len, 
                                        " " * (width - fill_len), delimiter, 
                                        rlabel)
        print to_print
    print "%s%s+%s" % (" " * (max_label_len + 2), "-" * zero, "-" * (width - zero))
    if write_axis_labels:
        llabel = str(min_value)
        rlabel = str(max_value)
        loffset = max_label_len + 1 - (len(llabel) / 2)
        roffset = width + max_label_len + 2 - (loffset + len(llabel))
        to_print = "%s%s%s%s" % (" " * loffset, llabel, " " * roffset, rlabel)
        print to_print
    print


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
    draw_graph(vals, write_axis_labels=True, write_values=True, title="Monthly Chart")
