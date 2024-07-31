function Assert-AreEqual
{
    param([object] $expected, [object] $actual, [string] $message)
  
  if (!$message)
  {
      $message = "Assertion failed because expected '$expected' does not match actual '$actual'"
  }
  
  if ($expected -ne $actual) 
  {
      throw $message
  }
  
  return $true
}

# Tester help
# python .\mypgp.py -h

# Tester xor
$res = echo "68656c6c6f20776f726c64" | python .\mypgp.py -xor -c -b 7665727920736563726574
$normalRes = "1e001e154f53120c000910"
Assert-AreEqual $res $normalRes

$res = echo "1e001e154f53120c000910" | python .\mypgp.py -xor -d -b 7665727920736563726574
$normalRes = "68656c6c6f20776f726c64"
Assert-AreEqual $res $normalRes

$res = echo "68656c6c6f20776f726c64" | python .\mypgp.py -xor -c abcd
$normalRes = "c3a8c7a1c4eddca2d9a1cf"
Assert-AreEqual $res $normalRes

#Tester AES
# echo "c2486f4796f0657481a655c559b38aaa" | python .\mypgp.py -aes -c -b 6b50fd39f06d33cfefe6936430b6c94f
$res = echo "c2486f4796f0657481a655c559b38aaa" | python .\mypgp.py -aes -c -b 6b50fd39f06d33cfefe6936430b6c94f
$normalRes = "93ffded914573504eb79ac51e46777aa"
Assert-AreEqual $res $normalRes

# echo "0fc668acd39462d17272fe863929973a" | python .\mypgp.py  -aes -d -b 6b50fd39f06d33cfefe6936430b6c94f
$res = echo "93ffded914573504eb79ac51e46777aa" | python .\mypgp.py  -aes -d -b 6b50fd39f06d33cfefe6936430b6c94f
$normalRes = "c2486f4796f0657481a655c559b38aaa"
Assert-AreEqual $res $normalRes

$res = echo "c2486f4796f0657481a655c559b38aaa" | python .\mypgp.py -aes -c 6b50fd39f06d33cfefe6936430b6c94f
$normalRes = "bef536cdf978dc0e983f530187da958593ffded914573504eb79ac51e46777aa"
Assert-AreEqual $res $normalRes

$res = echo "bef536cdf978dc0e983f530187da958593ffded914573504eb79ac51e46777aa" | python .\mypgp.py -aes -d 6b50fd39f06d33cfefe6936430b6c94f
$normalRes = "c2486f4796f0657481a655c559b38aaa"
Assert-AreEqual $res $normalRes

# Tester RSA

python .\mypgp.py -rsa -g d3 e3
# python .\mypgp.py -rsa -g 4b1da73924978f2e9c1f04170e46820d648edbee12ccf4d4462af89b080c86e1 bb3ca1e126f7c8751bd81bc8daa226494efb3d128f72ed9f6cacbe96e14166cb
echo "c1fa29d40054f3fcb1c15fe4d63d3887" | python .\mypgp.py -rsa -c 010001-c9f91a9ff3bd6d84005b9cc8448296330bd23480f8cf8b36fd4edd0a8cd925de139a0076b962f4d57f50d6f9e64e7c41587784488f923dd60136c763fd602fb3
echo "dc0bd7367d04e5a9e9e14467ff38de0625b3cfa5aabbe86def48bfc93e97aab713d70abf83d263a6dd6570c6d297cc44bad2e0dd2cf7b4c3e0a9749d68ca11a8" | python .\mypgp.py -rsa -d 81b08f4eb6dd8a4dd21728e5194dfc4e349829c9991c8b5e44b31e6ceee1e56a11d66ef23389be92ef7a4178470693f509c90b86d4a1e1831056ca0757f3e209-c9f91a9ff3bd6d84005b9cc8448296330bd23480f8cf8b36fd4edd0a8cd925de139a0076b962f4d57f50d6f9e64e7c41587784488f923dd60136c763fd602fb3

Get-Content .\MESSAGE_FILE.txt | python .\mypgp.py -pgp -c 010001-c9f91a9ff3bd6d84005b9cc8448296330bd23480f8cf8b36fd4edd0a8cd925de139a0076b962f4d57f50d6f9e64e7c41587784488f923dd60136c763fd602fb3 > CIPHERT.txt
cat .\CIPHERT.txt 

Get-Content .\CIPHERT.txt | python .\mypgp.py -pgp -d 81b08f4eb6dd8a4dd21728e5194dfc4e349829c9991c8b5e44b31e6ceee1e56a11d66ef23389be92ef7a4178470693f509c90b86d4a1e1831056ca0757f3e209-c9f91a9ff3bd6d84005b9cc8448296330bd23480f8cf8b36fd4edd0a8cd925de139a0076b962f4d57f50d6f9e64e7c41587784488f923dd60136c763fd602fb3

# $res = $res -replace " ", "`n"
# $bytes = [System.Text.Encoding]::UTF8.GetBytes($res)
# $hexRepresentation = [BitConverter]::ToString($bytes) -replace '-'
# Write-Host $bytes
# echo "public key: 010001-19bb`nprivate key: 81b3-19bb" > tmp1.txt
# Assert-AreEqual $res $normalRes

# $res = echo "2a" | python .\mypgp.py -rsa -c 010001-19bb
# $normalRes = "b104"
# Assert-AreEqual $res $normalRes
