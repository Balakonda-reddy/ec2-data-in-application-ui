
awk 'BEGIN{
    FS=","
    print "<TABLE border=2>"
}
{
    print   "<TR>"
    for(i=1;i<=NF;i++)
    {
        if(NR==1)
          print "<th>" $i "</th>"
        else
          print "<td>" $i "</td>" 
    }       
    print "</TR>"       
}
END{
    print "</TABLE>>"
}' ec2_list_all.csv > ACCOUNT-1.html