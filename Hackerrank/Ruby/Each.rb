#/*
#By: Ahmed Moustafa (a.k.a geekahmed)
#Email: geekahmed1@gmail.com
#linkedIn: https://www.linkedin.com/in/geekahmed
#*/


def scoring(array)
    # iterate through each of the element in array using *each* and call update_score on it
    array.each do |user|
        user.update_score
    end
end
