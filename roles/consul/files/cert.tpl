{{ with secret "pki/internal/issue/consul" "common_name=consul.service.consul" }}
{{ .Data.certificate }}{{ end }}
