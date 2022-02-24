ta Types In python...!
        
        num = 2.5
                
                type(num)
                        
                        <class 'float'>
                        num = 7
                                
                                type(num)
                                        
                                        <class 'int'>
                                        #for complex numbers...
                                                
                                                num = 6+9j
                                                        
                                                        type(num)
                                                                
                                                                <class 'complex'>
                                                                a = 5.6
                                                                        
                                                                        b = int(a)
                                                                                
                                                                                type(b)
                                                                                        
                                                                                        <class 'int'>
                                                                                        b
                                                                                                
                                                                                                5
                                                                                                k = float(b)
                                                                                                        
                                                                                                        k
                                                                                                                
                                                                                                                5.0

                                                                                                                k = 6
                                                                                                                        
                                                                                                                        c = complex(b, k)
                                                                                                                                
                                                                                                                                c
                                                                                                                                        
                                                                                                                                        (5+6j)

                                                                                                                                        b<k
                                                                                                                                                
                                                                                                                                                True

                                                                                                                                                bool = b < k
                                                                                                                                                        

                                                                                                                                                        bool
                                                                                                                                                                
                                                                                                                                                                True

                                                                                                                                                                type(bool)
                                                                                                                                                                        
                                                                                                                                                                        <class 'bool'>

                                                                                                                                                                        b > k
                                                                                                                                                                                
                                                                                                                                                                                False

                                                                                                                                                                                int(True)
                                                                                                                                                                                        
                                                                                                                                                                                        1

                                                                                                                                                                                        int(False)
                                                                                                                                                                                                
                                                                                                                                                                                                0

                                                                                                                                                                                                lst = [25, 36, 45, 12]
                                                                                                                                                                                                        
                                                                                                                                                                                                        type(lst)
                                                                                                                                                                                                                
                                                                                                                                                                                                                <class 'list'>

                                                                                                                                                                                                                s = {23, 45, 78, 43, 55, 67}
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        s
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                {67, 55, 23, 43, 45, 78}

                                                                                                                                                                                                                                type(s)
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        <class 'set'>

                                                                                                                                                                                                                                        t = (34, 56, 78, 86, 44, 23)
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                type(t)
                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                        <class 'tuple'>

                                                                                                                                                                                                                                                        str="tyron"
                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                st = 't
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        SyntaxError: unterminated string literal (detected at line 1)
                                                                                                                                                                                                                                                                        st = 't'
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                type(st)
                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                        <class 'str'>

                                                                                                                                                                                                                                                                                        range(0, 10)
                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                range(0, 10)

                                                                                                                                                                                                                                                                                                range(10)
                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                        range(0, 10)

                                                                                                                                                                                                                                                                                                        list(range(10))
                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                                                                                                                                                                                                                                                                                                                list(range(2, 10, 2))
                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                        [2, 4, 6, 8]

                                                                                                                                                                                                                                                                                                                        type(range(10))
                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                <class 'range'>

                                                                                                                                                                                                                                                                                                                                d = {'tyron': 'apple', 'ravi': 'samsung', 'surya': 'xiomi'}
                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                        d
                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                {'tyron': 'apple', 'ravi': 'samsung', 'surya': 'xiomi'}
                                                                                                                                                                                                                                                                                                                                                d.keys()
                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                        dict_keys(['tyron', 'ravi', 'surya'])

                                                                                                                                                                                                                                                                                                                                                        d.values()
                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                dict_values(['apple', 'samsung', 'xiomi'])

                                                                                                                                                                                                                                                                                                                                                                d['surya']
                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                        'xiomi'

                                                                                                                                                                                                                                                                                                                                                                        d.get('ravi')
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                'samsung'

                                                                                                                                                                                                                                                                                                                                                                                d.get('tyron')
                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                        'apple'
