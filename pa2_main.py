if __name__ == "__main__":
    cap_join = ["calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars"]
    print(cap_join)
    def cap_join(string_list):
        cap_join = ["calvin"]
        new_list = cap_join
        for i in string_list:
            new_list.append(i[:1].upper() + i[1:])
        return "".join(new_list)



















