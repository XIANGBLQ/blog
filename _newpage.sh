#!/bin/bash

# This script standardize the procedure to create a page.

# Page Title
function get_page_title() {
  echo "page title: "
  read -p "> " title
}

# Date
function get_date() {
  create_date=`date "+%Y-%m-%d %H:%M"`
  year=`date "+%Y"`
} 

# Tags
function get_tags() {
  echo "choose tags: "
  ls -1p tag/ | grep '/$' | sed 's/\/$//' | sort | column
  read -p "> " tags
}

# Category
function get_category() {
  echo "choose a category: "
  ls -1p _content/ | grep '/$' | sed 's/\/$//' | sort | column
  read -p "> " category
}

# fields to generate
function set_file_name() {
  slugify_title=`echo "${title}" | sed -e 's/[^[:alnum:]]/-/g' | tr -s '_' | tr A-Z a-z.`
  filedir="_content/${category}/${year}"
  filename="${filedir}/${slugify_title}.md"
}

function create_file() {
  mkdir -p $filedir
  tmpfile="/tmp/newpage.template.${RANDOM}"
  echo "create tmpfile: ${tmpfile}"
  eval "echo \"$(cat _scripts/templates/page.md)\"" > $tmpfile
  vi $filename -c "read ${tmpfile}"
  rm $tmpfile
}

# confirm information
function confirm_info() {
  echo
  echo "Page Title: ${title}"
  echo "Date: ${create_date}"
  echo "Tags: ${tags}"
  echo "Category: ${category}"
  echo "Page file: ${filename}"
  echo 
  read -p "Are you sure to create the page?(Y/n) " confirm
 
  if [[ $confirm =~ ^[Yy]$ ]] || [[ $confirm =~ ^$ ]]
  then   
    create_file
  fi

}



get_page_title
get_date
get_tags
get_category
set_file_name
confirm_info


