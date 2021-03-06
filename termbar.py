class TermBar(object):
    # Lines of margin to print
    MARGIN_TOP = 1
    MARGIN_BOTTOM = 1

    def __init__(self, series = [], 
                 width=40, 
                 title="", 
                 write_labels=False, 
                 write_axis_labels=False, 
                 write_values=False, 
                 fill_char="#", 
                 delim="!", 
                 y_axis_mark='|'):
        self.series = series
        self.width = width
        self.title = title
        self.write_labels = write_labels
        self.write_axis_labels = write_axis_labels
        self.write_values = write_values
        self.fill_char = fill_char
        self.delim = delim
        self.y_axis_mark = y_axis_mark

    def draw(self):
        """
        Draws a left-right bar graph in the terminal
        """
        print "\n".join(self.get_graph())

    def get_graph(self):
        if self.write_labels:
            max_label_len = max([len(s[0]) for s in self.series])
        else:
            max_label_len = 0
        left_offset = max_label_len + 2
        max_value = max([s[1] for s in self.series])
        min_value = min([s[1] for s in self.series])
        if min_value > 0:
            min_value = 0
        val_range = max_value - min_value
        if not val_range:
            maxmin = abs(int(1.2 * min_value))
            val_range = 2 * maxmin
            min_value = -maxmin
            max_value = maxmin
        lines = []
        lines.append(self.get_top_margin())
        lines.append(self.get_title(left_offset))
        zero = int(self.width * (float(0 - min_value) / val_range))
        lines.append(self.get_graph_top(left_offset, zero))
        for label, value in self.series:
            if self.write_labels:
                lpad = max_label_len - len(label)
                label_str = self.repeat_seq_str([(" ", lpad),
                                                 (label, 1),
                                                 (" ", 1)])
            else:
                label_str = " "
            if self.write_values:
                rlabel = " %s" % (value,)
            else:
                rlabel = ""
            fill_len = int(self.width * (float(value) / val_range))
            chart_str = self.get_chart_str(zero, fill_len)
            to_print = "%s%s%s%s%s" % (label_str, self.delim, 
                                       chart_str, self.delim, 
                                       rlabel)
            lines.append(to_print)
        lines.append(self.get_graph_bottom(left_offset, zero))
        if self.write_axis_labels:
            llabel = str(min_value)
            rlabel = str(max_value)
            loffset = max_label_len + 1 - (len(llabel) / 2)
            roffset = self.width + left_offset - (loffset + len(llabel))
            to_print = self.repeat_seq_str([
                                            (" ", loffset), 
                                            (llabel, 1),
                                            (" ", roffset),
                                            (rlabel, 1)
                                           ])
            lines.append(to_print)
        lines.append(self.get_bottom_margin())
        return lines

    def get_chart_str(self, zero, fill_len):
        if fill_len < 0:
            chart_str = self.repeat_seq_str([
                                        (" ", (zero + fill_len)), 
                                        (self.fill_char, -fill_len), 
                                        (self.y_axis_mark, 1), 
                                        (" ", (self.width - zero))
                                       ])
        else:
            chart_str = self.repeat_seq_str([
                                        (" ", (zero)), 
                                        (self.y_axis_mark, 1), 
                                        (self.fill_char, fill_len), 
                                        (" ", (self.width - zero - fill_len))
                                       ])
        return chart_str

    def repeat_seq_str(self, seqs):
        fmt_str = "%s" * len(seqs)
        return fmt_str % tuple((x * y for x, y in seqs))

    def get_graph_top(self, left_offset, zero):
        return self.get_graph_horiz(left_offset, zero, "_")

    def get_graph_bottom(self, left_offset, zero):
        return self.get_graph_horiz(left_offset, zero, "-")

    def get_graph_horiz(self, left_offset, zero, line_char):
        return self.repeat_seq_str([
                                (" ", left_offset), 
                                (line_char, zero), 
                                (self.y_axis_mark, 1), 
                                (line_char, (self.width - zero))
                             ])

    def get_title(self, left_offset):
        if self.title:
            lpad = (self.width - len(self.title)) / 2
            return self.repeat_seq_str([
                                        (" ", left_offset), 
                                        (" ", lpad),
                                        (self.title,1),
                                      ])
        else:
            return ""

    def get_top_margin(self):
        return "\n" * self.MARGIN_TOP

    def get_bottom_margin(self):
        return "\n" * self.MARGIN_BOTTOM
