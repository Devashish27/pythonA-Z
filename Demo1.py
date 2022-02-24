 Lists IN python..!
nums = [43, 25, 63, 21, 56]
nums[0]


ceback (most recent call last):
      File "<pyshell#21>", line 1, in <module>
          nums[45]
          IndexError: list index out of range






          nums[3]
          89

          nums[2:]
          [78, 89, 54, 23]

          nums[-1]
          23

          nums[-5]
          45

          names = ['gary', 'Arun', 'Devashish']
          names
          ['gary', 'Arun', 'Devashish']

          values = [4.5, 'tiyfd', 23]

          mil = [nums, names]

          mil
          [[23, 45, 78, 89, 54, 23], ['gary', 'Arun', 'Devashish']]

          nums.append(56)

          mnums
          Traceback (most recent call last):
                File "<pyshell#47>", line 1, in <module>
                    mnums
                    NameError: name 'mnums' is not defined. Did you mean: 'nums'?

                    nums
                    [23, 45, 78, 89, 54, 23, 56]

                    nums.insert(2, 56)
                    nums
                    [23, 45, 56, 78, 89, 54, 23, 56]

                    nums.remove
                    <built-in method remove of list object at 0x000002E601AF6080>
                    nums.remove(23)

                    nums
                    [45, 56, 78, 89, 54, 23, 56]

                    nums.pop()
                    56

                    # For deleting multiple values
                    nums
                    [45, 56, 78, 89, 54, 23]

                    nums.extend
                    <built-in method extend of list object at 0x000002E601AF6080>
                    nums.extend(90, 19, 067, 7895)
                    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
                    nums.extend[(90, 19, 067, 78, 95)]
                    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
                    nums.extend[(90, 19, 67, 78, 95)]
                    Traceback (most recent call last):
                          File "<pyshell#67>", line 1, in <module>
                              nums.extend[(90, 19, 67, 78, 95)]
                              TypeError: 'builtin_function_or_method' object is not subscriptable
                              max(nums)
                              89
                              sum(nums)
                              345

                              nums.sort()
                              nums
                              [23, 45, 54, 56, 78, 89]
