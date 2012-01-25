class TermBar(object):
    MARGIN_TOP = 1
    MARGIN_BOTTOM = 1

    def __init__(self, series = [], width=40, title="", write_axis_labels=False, 
               write_values=False, fill_char="#", delim="|", y_axis_mark='|'):
        self.series = series
        self.width = width
        self.title = title
        self.write_axis_labels = write_axis_labels
        self.write_values = write_values
        self.fill_char = fill_char
        self.delim = delim
        self.y_axis_mark = '|'

    def draw(self):
        """
        Draws a left-right bar graph in the terminal
        series should be a list of tuples:
            (label, value)
        """
        max_label_len = max([len(s[0]) for s in self.series])
        left_offset = max_label_len + 2
        max_value = max([s[1] for s in self.series])
        min_value = min([s[1] for s in self.series])
        val_range = max_value - min_value
        self.print_top_margin()
        self.print_title(left_offset)
        zero = int(self.width * (float(0 - min_value) / val_range))
        self.print_graph_top(left_offset, zero)
        for label, value in self.series:
            lpad = max_label_len - len(label)
            if self.write_values:
                rlabel = " %s" % (value,)
            else:
                rlabel = ""
            fill_len = int(self.width * (float(abs(value)) / val_range))
            if value < 0:
                chart_str = "%s%s%s%s" % (" " * (zero - fill_len), "#" * fill_len, self.y_axis_mark, " " * (self.width - zero))
            else:
                chart_str = "%s%s%s%s" % (" " * (zero), self.y_axis_mark, "#" * fill_len, " " * (self.width - zero - fill_len))
            to_print = "%s%s %s%s%s%s" % (" " * lpad, label, self.delim, 
                                            chart_str, self.delim, 
                                            rlabel)
            print to_print
        self.print_graph_bottom(left_offset, zero)
        if self.write_axis_labels:
            llabel = str(min_value)
            rlabel = str(max_value)
            loffset = max_label_len + 1 - (len(llabel) / 2)
            roffset = self.width + left_offset - (loffset + len(llabel))
            to_print = "%s%s%s%s" % (" " * loffset, llabel, " " * roffset, rlabel)
            print to_print
        self.print_bottom_margin()

    def repeat_seq_str(self, seqs):
        fmt_str = "%s" * len(seqs)
        return fmt_str % tuple((x * y for x, y in seqs))

    def print_graph_top(self, left_offset, zero):
        self.print_graph_horiz(left_offset, zero, "_")

    def print_graph_bottom(self, left_offset, zero):
        self.print_graph_horiz(left_offset, zero, "-")

    def print_graph_horiz(self, left_offset, zero, line_char):
        print self.repeat_seq_str([
                                (" ", left_offset), 
                                (line_char, zero), 
                                (self.y_axis_mark, 1), 
                                (line_char, (self.width - zero))
                             ])

    def print_title(self, left_offset):
        if self.title:
            print "%s%s%s" % (" " * left_offset, 
                              " " * ((self.width - len(self.title))/2), 
                              self.title)

    def print_top_margin(self):
        print "\n" * self.MARGIN_TOP

    def print_bottom_margin(self):
        print "\n" * self.MARGIN_BOTTOM


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
    a = TermBar(vals, write_axis_labels=True, write_values=True, title="Monthly Chart")
    a.draw()
