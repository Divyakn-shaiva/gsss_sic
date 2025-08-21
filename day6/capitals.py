def kaprekar_process(num):
    print(f"\nStarting number: {num}")
    seen = set()

    while num != 6174:
        # Always keep 4 digits (with leading zeros if needed)
        s = str(num).zfill(4)

        # Arrange digits
        desc = int("".join(sorted(s, reverse=True)))
        asc = int("".join(sorted(s)))

        # Do subtraction
        diff = desc - asc
        print(f"{desc:04d} - {asc:04d} = {diff:04d}")

        if diff in seen:   # prevent infinite loop
            print("Loop detected, stopping.")
            break

        seen.add(diff)
        num = diff

    if num == 6174:
        print("Reached Kaprekar constant: 6174 🎉")


# ----------- MAIN PROGRAM ------------
n = int(input("Enter a 4-digit number: "))
kaprekar_process(n)
