for file in `ls *.jpg`
do 
    height=`identify $file|awk '{print $3}'|awk -v FS=x '{print $2}'`
    if [[ $[$height%2] -eq 1 ]];then
        height=$[$height-1]
        width=`identify $file|awk '{print $3}'|awk -v FS=x '{print $1}'`
        convert -resize ${width}x${height}! $file $file
    fi
done
