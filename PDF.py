"""
@author:SC
@file:PDF.py
@time:2020/05/05
"""



async =  require 'async'
 
fs = require 'fs'

#write file
writeFile = (address, str, cbf) ->
  write = fs.writeFileSync(address,str)
  return cbf null, write

#generate html file
htmlFile = (address, option, cbf) ->
  html = fs.readFileSync(address,option)
  return cbf null, html

#generate pdf file
pdfFile = (html, address, cbf) ->
  # console.log "html",html
  options = { format: 'A3' }
  pdf.create html, options
    .toFile address, (err, res) ->
      if (err) 
        return console.log err
      return cbf null,"success"

#delete html file
deteleHtml = (address, cbf) ->
  fs.unlink address, (err,res) ->
    if (err) 
      return console.log err
    return cbf null, 'detele success'

#get file

funcs = [
  # Write file
  (cbf) ->
    return writeFile htmlAdr, params.str, cbf
  # generate html file
  (result1,cbf) ->
    return htmlFile htmlAdr, 'utf-8', cbf
  # generate pdf file
  (result2,cbf) ->
    return pdfFile result2, pdfAdr, cbf
  # Delete html file
  (result3,cbf) ->
    return deteleHtml htmlAdr, cbf
]
async.waterfall funcs, (error, result) ->
  if error
    return cbf error, null
  # return user's information
  res.download pdfAdr, fileName