{
  "targets": [
    {
      "target_name": "rabin-bindings",
      "conditions": [
          ["OS == 'win'", {
              "defines": [
                  "_HAS_EXCEPTIONS=0"
              ],
              "msvs_settings": {
                  "VCCLCompilerTool": {
                      "RuntimeTypeInfo": "false"
                    , "EnableFunctionLevelLinking": "true"
                    , "ExceptionHandling": "2"
                    , "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244", "4506" ]
                  }
              },
              'include_dirs': [
                'src/win/'
              ]
          }],
        
          ["OS == 'mac'", {
              "xcode_settings": {
                "OTHER_CPLUSPLUSFLAGS": [
                  "-stdlib=libc++"
                ],
                "OTHER_LDFLAGS": [
                  "-stdlib=libc++"
                ]
              }
          }]
      ],
      "sources": [ "bindings.cc", "src/rabin.cc", "src/rabin_wrap.cc"],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
      ],
    },
  ]
}
