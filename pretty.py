def prettify(j, d = "\t"):

    j = list(j)     # Char list
    l = len(j)      # Length
    p = 0           # Position
    i = 0           # Indentation
    b = ""          # Buffer
    n = 0           # Newline switch, set to 1 whenever we are not on a clean newline.

    while p < l:
        c = j[p]

        # Ignore all whitespace chars out of quotes.
        if c in " \n\t":
            p += 1
            continue

        # Start block adds newline, increments indentation size (i) and position (p)
        if c in "{[":
            b += ("\n"*n) + d*i*n
            i += 1
            b += c + "\n" + d*i
            p += 1
            n = 0
            continue

        # If we find a quote, buffer chars until next quote.
        if c in "\"\'":

            # Store start quote.
            q = c

            while c != q:
                b += c

                # If we just buffered a backslash, buffer following char blindly and increment p.
                if c == "\\":
                    p += 1
                    b += j[p]

                p += 1
                c = j[p]

        # End block decrements indentation size, adds new line and idents.
        if c in "}]":
            i -= 1
            b += "\n" + (d*i)
            n = 0

        # Buffer char.
        b += c
        n = 1

        # A comma generates a new line on current indentation level.
        if c == ",":
            b += "\n"*n + (d*i)
            n = 0


        # A colon should be appended by a space.
        elif c == ":":
            b += " "

        p += 1

    return b

    pass


json = '    {         "permissions":   {{{   \'group\':null,"test":""}}},         "patch":{"user":"pomle","comment":"Preview","saleperiods":[{"service":"subscription"},{"service":"ad","start":"2013-01-24","countries":"SE DK"}]}}'

print prettify(json)