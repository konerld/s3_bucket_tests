#!/bin/python
var_dict ={
	"accesskey" : "akey6",
        "secretkey" : "privkey6",
        "endpoint" : "http://10.2.124.6:9007",
        "cprefix" : "s3testqwer",
        "sizes" : "c(100)MB",
        "rw_workers" : "2",
        "rw_runtime" : "30",
	"prepare_objects" : "1,100",
        "read_objects" : "1,50",
	"write_objects" : "51,100",
	"cleanup_onjects" : "1,100"
	}

def make_xml(var_dict):
    source = """<?xml version="1.0" encoding="UTF-8" ?>
<workload name="s3-sample" description="sample benchmark for s3">

  <storage type="s3" config="accesskey={accesskey};secretkey={secretkey};proxyhost=;proxyport=;endpoint={endpoint}" />
    
  <workflow>
    
    <workstage name="init">
      <work type="init" workers="1" config="cprefix={cprefix};containers=r(1,2)" />
    </workstage>
    
    <workstage name="prepare">
      <work type="prepare" workers="1" config="cprefix={cprefix};containers=r(1,2);objects=r({prepare_objects});sizes={sizes}" />
    </workstage>
    
    <workstage name="main">
      <work name="main" workers="{rw_workers}" runtime="{rw_runtime}">
        <operation type="read" ratio="80" config="cprefix=s3testqwer;containers=u(1,2);objects=u({read_objects})" />
        <operation type="write" ratio="20" config="cprefix=s3testqwer;containers=u(1,2);objects=u({write_objects});sizes={sizes}" />
        </work>
    </workstage>
    
    <workstage name="cleanup">
      <work type="cleanup" workers="1" config="cprefix={cprefix};containers=r(1,2);objects=r({cleanup_onjects})" />
    </workstage>
    
    <workstage name="dispose">
      <work type="dispose" workers="1" config="cprefix=s3testqwer;containers=r(1,2)" />
    </workstage>
    
  </workflow>
    
</workload>""".format(**var_dict)

    with open('s3_test.xml','w') as f:
        f.write(source)

def main():
    make_xml(var_dict)

if __name__ == "__main__":
        main()
