#/*
#By: Ahmed Moustafa (a.k.a geekahmed)
#Email: geekahmed1@gmail.com
#linkedIn: https://www.linkedin.com/in/geekahmed
#*/


def odd_or_even(number)

    # add your code here
    return number.even?
end

(0...gets.to_i).each do |i|
    puts odd_or_even(gets.to_i)
end

